import pdftotext


def load_file():
    with open(
        "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storagePdfFiles//Amit Nautiyal CV nov 2020.pdf",
        "rb",
    ) as f:
        pdf = pdftotext.PDF(f)
    return pdf


file = load_file()
file1 = open(
    "//home//amit//Amit work environment//NLP_for _doc_search//documentsStorage//storageTextFiles//Amit Nautiyal CV nov 2020.txt",
    "w",
)
for i in range(len(file)):
    file1.write(file[i])
file1.close()


if __name__ == "__main__":
    load_file()
