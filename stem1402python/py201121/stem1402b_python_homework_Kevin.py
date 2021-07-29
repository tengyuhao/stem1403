"""
Homework
"""

#
try:
    print("Start opening file...")

    filepath = "../py201121/tc_qc_csv_fra.csv"
    print("\t"+filepath)

    file = open(filepath, encoding="utf-8")

    print("==================")
    content = file.read()
    print(content)
    print("==================")
    print()

    print("Closing...")
    file.close()

    print("Done.")

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except UnicodeDecodeError as ude:
    print(ude)

except Exception as e:
    print(e)

try:
    print("Start opening file...")

    filepath = "../py201128/test_html.html"
    print("\t"+filepath)

    file = open(filepath, encoding="utf-8")


    print("==================")
    content = file.read()
    print(content)
    print("==================")
    print()

    print("Closing...")
    file.close()

    print("Done.")
except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except UnicodeDecodeError as ude:
    print(ude)

except Exception as e:
    print(e)


