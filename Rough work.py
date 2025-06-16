def largestnumber(numlist):
    s = 0
    while (len(numlist)!=0):
        s = s * 100 + max(numlist)
        numlist.remove (max(numlist))
    return s
numlist = [23,34,57]
largernumber = largestnumber(numlist)
print(largestnumber)

def find_matching_file(config_name, single_version_files, multi_version_files, selected_version):
    # 🔁 In-place decoding replacements
    replacements = {
        "&": "and",
        "@": "at",
        "%": "percent",
        "$": "dollar",
        "#": "number",
        "+": "plus",
        "-": "",       # optional: remove dashes
        " ": "",       # optional: remove spaces
    }

    for symbol, replacement in replacements.items():
        config_name = config_name.replace(symbol, replacement)

    normalized_key = normalize_text(config_name)

    if normalized_key in single_version_files:
        return [single_version_files[normalized_key][0]]

    elif normalized_key in multi_version_files:
        candidates = multi_version_files[normalized_key]
        dated = [(f, extract_date_from_filename(f)) for f in candidates]
        dated.sort(key=lambda x: (x[1] or datetime.min))

        if selected_version == 'latest':
            print(f"✅ Latest version selected: {dated[-1][0]}")
            return [dated[-1][0]]
        elif selected_version == 'oldest':
            print(f"✅ Oldest version selected: {dated[0][0]}")
            return [dated[0][0]]
        else:
            print(f"✅ All versions selected: {[f for f, _ in dated]}")
            return [f for f, _ in dated]

    print("❌ No match found.")
    return []

