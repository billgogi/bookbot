  
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        print(f"{contents}")

def main():
    get_book_text()

main()
