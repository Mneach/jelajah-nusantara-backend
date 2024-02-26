def extractFindAllData(arr):
    paragraph = []
    for data in arr:
        text = data.text.strip()
        paragraph.append(text)
    return paragraph