from tag2bio import Tag2Bio, Bio2Tag

def main():
    text = """My name is <name>John Doe</name>. and this is just an
    example for the demonstration in <country>Brazil</country>.
    """
    
    output_path = './output.txt'

    tb = Tag2Bio(text)
    parsed = tb.parse()
    
    print(parsed)

    # tb.save(output_path)

    bt = Bio2Tag(parsed)
    bio_parsed = bt.parse()

    print(bio_parsed)

    bt.save()

if __name__ == '__main__':
    main() 

