import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
from .forms import UploadFileForm

def analyze_csv(file):
    df = pd.read_csv(file)

    # First five rows of the dataset
    first_rows = df.head().to_html(classes='table table-striped')

    # Summary statistics for the entire DataFrame
    summary_stats = df.describe().to_html(classes='table table-striped')

    # Handling missing values
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]  # Only show columns with missing values
    missing_values = pd.DataFrame(missing_values, columns=['Missing Values'])  # Convert to DataFrame
    missing_values_html = missing_values.to_html(classes='table table-striped')

    # Data Visualizations
    plots = []

    # Histograms for numerical columns
    for column in df.select_dtypes(include='number').columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column], kde=True, color='skyblue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plots.append(encode_plot_to_base64())

    # Box plots for numerical columns
    for column in df.select_dtypes(include='number').columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=df[column], color='lightcoral')
        plt.title(f'Box plot of {column}')
        plt.ylabel(column)
        plots.append(encode_plot_to_base64())

    # Scatter plots for numerical columns (pairwise)
    num_columns = df.select_dtypes(include='number').columns
    if len(num_columns) > 1:
        plt.figure(figsize=(10, 8))
        sns.pairplot(df[num_columns])
        plt.suptitle('Pairwise Scatter Plots', y=1.02)
        plots.append(encode_plot_to_base64())

    return first_rows, summary_stats, missing_values_html, plots

def encode_plot_to_base64():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            first_rows, summary_stats, missing_values_html, plots = analyze_csv(file)
            return render(request, 'dataapp/results.html', {
                'first_rows': first_rows,
                'summary_stats': summary_stats,
                'missing_values': missing_values_html,
                'plots': plots
            })
    else:
        form = UploadFileForm()
    return render(request, 'dataapp/upload.html', {'form': form})
