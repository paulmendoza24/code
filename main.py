def main():
    import pyfiglet
    def add_definition(term, meaning, usage):
        return {
            "term": term,
            "meaning": meaning,
            "usage": usage
        }
    var = pyfiglet.figlet_format("Definition Stored")
    term = input("Enter a term: ")
    meaning = input(f"Enter the Meaning of {term}: ")
    usage = input(f"Enter the usage of {term}: ")

    glossary = add_definition(term, meaning, usage)

    print("-"*60)
    print("\nMendoza, Niño Paul C.")
    print(var)
    print(f"Term: {glossary['term']}")
    print(f"Meaning: {glossary['meaning']}")
    print(f"Usage: {glossary['usage']}")
    print("-"*60)


if __name__ == "__main__":
    main()
