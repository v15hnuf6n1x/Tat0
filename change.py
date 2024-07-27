import re

def change_domain(url):
    # List of words to look for in the domain
    keywords = ['1024tera', 'terabox', 'nephobox']
    # Target domain to replace with
    target_domain = 'www.freeterabox.com'

    # Extract the domain from the URL
    domain_pattern = re.compile(r'https?://([^/]+)')
    match = domain_pattern.match(url)
    if not match:
        return url  # Return the original URL if it doesn't match the pattern

    domain = match.group(1)

    # Check if the domain contains any of the keywords
    for keyword in keywords:
        if keyword in domain:
            # Replace the domain with the target domain
            new_url = re.sub(r'https?://[^/]+', f'https://{target_domain}', url)
            return new_url

    # Return the original URL if no keywords are found
    return url

# Example usage
input_url = input("enter the input")
output_url = change_domain(input_url)
print("Original URL:", input_url)
print("Modified URL:", output_url)
