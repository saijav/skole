def read_dna_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        # Strip newlines from each line
        data = [line.strip() for line in data]
        return data
    except Exception as e:
        print(f"Error opening file {filename}: {e}")
        return []

def convert_to_dinucleotide(dna_seq):
    dinucleotides = []
    # Strip to dinucleotides
    for seq in dna_seq:
        for i in range(len(seq) - 1):
            dinucleotides.append(seq[i:i+2])
    return dinucleotides


def map_dins_to_int(dinucleotides):
    dinu_maps = {
        "AA": 1,
        "AC": 2,
        "AG": 3,
        "AT": 4,
        "CA": 5,
        "CC": 6,
        "CG": 7,
        "CT": 8,
        "GA": 9,
        "GC": 10,
        "GG": 11,
        "GT": 12,
        "TA": 13,
        "TC": 14,
        "TG": 15,
        "TT": 16
    }

    result = []

    for dinu in dinucleotides:
        if dinu in dinu_maps:
            result.append(dinu_maps[dinu])
        else:
            print(f"Warning: unknown dinucleotide: {dinu}")

    return result
