import streamlit as st
from ratelimit import limits, sleep_and_retry
import urllib.request
import xml.etree.ElementTree as ET

# Define rate limits
SEARCH_RATE_LIMIT = 2
RETRIEVAL_RATE_LIMIT = 5

@sleep_and_retry
@limits(calls=SEARCH_RATE_LIMIT, period=1)
def search_pubmed(topic, page):
    search_query = topic.replace(' ', '+')
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=xml'
    query_params = {'term': search_query, 'retstart': page*20, 'retmax': 20}
    search_url = base_url + '&' + urllib.parse.urlencode(query_params)
    
    with urllib.request.urlopen(search_url) as response:
        xml_response = response.read().decode('utf-8')

    root = ET.fromstring(xml_response)
    pmids = [id.text for id in root.findall('.//Id')]

    return pmids

@sleep_and_retry
@limits(calls=RETRIEVAL_RATE_LIMIT, period=1)
def retrieve_paper_details(pmid):
    summary_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=xml'
    with urllib.request.urlopen(summary_url) as response:
        xml_response = response.read().decode('utf-8')

    root = ET.fromstring(xml_response)
    title = root.find('.//Item[@Name="Title"]').text
    journal = root.find('.//Item[@Name="FullJournalName"]').text
    pub_date = root.find('.//Item[@Name="PubDate"]').text
    
    # Now let's retrieve the abstract as well
    abstract_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml&rettype=abstract'
    with urllib.request.urlopen(abstract_url) as response:
        abstract_xml = response.read().decode('utf-8')

    abstract_root = ET.fromstring(abstract_xml)
    abstract = abstract_root.find('.//AbstractText').text

    return {
        'title': title,
        'journal': journal,
        'pub_date': pub_date,
        'abstract': abstract,
        'pmid': pmid
    }

# Streamlit App
def main():
    st.title("PubMed Paper Scraper")
    topic = st.text_input("Enter the topic you want to search:", "machine learning in healthcare")
    
    if st.button("Search"):
        st.write(f"Searching for papers on: {topic}")
        pmids = search_pubmed(topic, 0)
        if pmids:
            st.write(f"Found {len(pmids)} papers. Displaying the first few:")
            for pmid in pmids[:5]:
                paper = retrieve_paper_details(pmid)
                st.subheader(paper['title'])
                st.write(f"**Journal:** {paper['journal']}")
                st.write(f"**Publication Date:** {paper['pub_date']}")
                st.write(f"**Abstract:** {paper['abstract']}")
                st.write(f"[Read more on PubMed](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']})")
                st.write("---")
        else:
            st.write("No papers found. Try a different search term.")

if __name__ == '__main__':
    main()
