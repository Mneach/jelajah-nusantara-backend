def extractFindAllData(arr):
    paragraph = []
    for data in arr:
        if data:
            text = data.text.strip()
            paragraph.append(text)
    return paragraph