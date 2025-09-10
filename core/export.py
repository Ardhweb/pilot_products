import weasyprint
from django.template.loader import render_to_string

def html_to_pdf(input_html, output_pdf, context_content=None):
    """
    Converts HTML string or HTML file (with optional Django context_content rendering) to PDF.

    Parameters:
    - input_html (str): The HTML file path or HTML string.
    - output_pdf (str): Path where the resulting PDF will be saved.
    - context_content (dict, optional): context_content for rendering HTML with Django templates. Default is None.
    """
    # Step 1: If context_content is provided, render the HTML with context_content
    if context_content:
        html_content = render_to_string(input_html, context_content)
    else:
        # If no context_content is provided, treat input_html as plain HTML or a file path
        if isinstance(input_html, str) and input_html.strip().startswith("<html"):
            html_content = input_html  # It's already an HTML string
        else:
            html_content = render_to_string(input_html)  # Treat it as a template path

    # Step 2: Convert the rendered HTML to PDF
    html = weasyprint.HTML(string=html_content)
    html.write_pdf(output_pdf)
    print(f"PDF saved at: {output_pdf}")

# Example Usage 1: Using an HTML string directly (no context_content)
# html_content = "<html><body><h1>Hello, WeasyPrint!</h1></body></html>"
# html_to_pdf(html_content, 'output_no_context_content.pdf')

# Example Usage 2: Using a template with context_content (optional)
# context_content = {
#     'name': 'Alice',
#     'message': 'This is a message with context_content!',
# }
# html_to_pdf('my_template.html', 'output_with_context_content.pdf', context_content)


def html_to_pdf_view(request, input_html, context_content=None):
    """
    Converts HTML string or HTML file (with optional Django context_content rendering) to PDF,
    and returns the PDF as an HTTP response.
    """
    if context_content:
        html_content = render_to_string(input_html, context_content)
    else:
        if isinstance(input_html, str) and input_html.strip().startswith("<html"):
            html_content = input_html  # It's already an HTML string
        else:
            html_content = render_to_string(input_html)  # Treat as template path

    html = weasyprint.HTML(string=html_content)
    pdf_content = html.write_pdf()  # Generate the PDF content

    # Return the PDF as an HTTP response
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="output.pdf"'
    return response