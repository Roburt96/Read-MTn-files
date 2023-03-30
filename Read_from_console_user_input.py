lines = []
result = {}
while True:
    line = input("Enter MT189 lines:")
    if line:
        lines.append(line)
    else:
        break

    current_key = ''
    for line in lines:
        if line.startswith(":"):

            try:
                key, value = line[1:].split(":")
                result[current_key.strip()].update({key.strip(): value.strip()})

            except:
                key, value = line[1:].split("::")
                result[current_key.strip()].update({key.strip(): value.strip()})

        else:
            current_key = line[1:-1].strip()
            result[current_key.strip()] = {}


    for key, value in result.items():
        print(key)
        for sub_key, sub_value in value.items():
            print(f"{sub_key} -> {sub_value}")




# TEST_INPUT_FILE = (
# -START MESSAGE-
# :20C::SEME//123456789
# :23G:NEWM
# :98C::PREP//20220330120015
# :16S:GENL
# -IDENTIFICATION-
# :20C::RELA//012345678
# :22F::TRTR//PAYM
# :22F::STCO//020
# :97A::SAFE//EXAMPLESAFE
# :94A::DEAL//BUYR/USD1,234,567.89
# :95P::BUYR//EXAMPLE BUYER NAME
# :95Q::SELL//EXAMPLE SELLER NAME
# :36B::QTYE//1,000,000
# :16S:TRADDET
# -SETTLEMENT INSTRUCTIONS-
# :98A::SETT//20220415
# :98A::PAYD//20220415
# :95R::REAG//EXAMPLE RECEIVER AGENT NAME
# :97A::SAFE//EXAMPLE SAFE NAME
# :16S:SETT
# -TRANSACTION DETAILS-
# :98A::TRAD//20220330
# :35B:ISIN US1234567890
# :16S:TRAN
# -TERMS AND CONDITIONS-
# :77H::TERP//EXAMPLE TERMS AND CONDITIONS
# :16S:TERMS
# -TRAILER-
# :16R:GENL
# :20C::SEME//123456789
# :23G:NEWM
# :16S:GENL
# :32B::CHDS//USD123456789.01
# :98C::VALU//20220330
# :92D::NEXT//20220415
# :16S:TRAILER
# )