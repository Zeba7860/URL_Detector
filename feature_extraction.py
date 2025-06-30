import re
import pandas as pd
import tldextract

def extract_features(url):
    return {
        'url_length': len(url),
        'num_digits': sum(c.isdigit() for c in url),
        'num_letters': sum(c.isalpha() for c in url),
        'num_special_chars': len(re.findall(r'\W', url)),
        'num_dots': url.count('.'),
        'has_ip': bool(re.match(r'(\d{1,3}\.){3}\d{1,3}', url)),
        'has_suspicious_words': any(word in url.lower() for word in ['login', 'free', 'click', 'verify']),
        'count_@': url.count('@'),
        'count_?': url.count('?'),
        'count_=': url.count('='),
        'tld': tldextract.extract(url).suffix
    }

def prepare_features(df):
    features = [extract_features(url) for url in df['url']]
    df_features = pd.DataFrame(features)
    df_features = pd.get_dummies(df_features, columns=['tld'])
    return df_features
