import re

all_inputs = ""

def parse_input(input_string):
    
    global all_inputs
    
    patterns = {
        'T': r'<T>(.*?)</T>',
        'NM': r'<NM>(.*?)</NM>',
        'SY': r'<SY>(.*?)</SY>',
        'CS': r'<CS>(.*?)</CS>',
        'TR': r'<TR>(.*?)</TR>',
        'PRE': r'<PRE>(.*?)</PRE>',
        'OP': r'<OP>(.*?)</OP>',
        'POS': r'<POS>(.*?)</POS>',
        'RT': r'<RT>(.*?)</RT>',
        'TRI': r'<TRI>(.*?)</TRI>',
        'TRD': r'<TRD>(.*?)</TRD>',
        'GNM': r'<GNM>(.*?)</GNM>',
        'TNM': r'<TNM>(.*?)</TNM>',
        'US': r'<US>(.*?)</US>',
        'SDE': r'<SDE>(.*?)</SDE>',
        'BP': r'<BP>(.*?)</BP>',
        'UBP': r'<UBP>(.*?)</UBP>',
    }

    # Extract the type
    type_match = re.search(patterns['T'], input_string)
    if not type_match:
        return []
    word_type = type_match.group(1)

    # Initialize the array based on the type
    if word_type == 'Disease' or word_type == "Injury":
        all_inputs += input_string + "\n"
        array = [None]*5  
        array[0] = word_type
        required_tags = ['NM', 'SY', 'CS', 'TR']
        indices = [1, 2, 3, 4]
    elif word_type == 'Operation':
        all_inputs += input_string + "\n"
        array = [None]*6  
        array[0] = word_type
        required_tags = ['NM', 'PRE', 'OP', 'POS', 'RT']
        indices = [1, 2, 3, 4, 5]
    elif word_type == 'Treatment':
        all_inputs += input_string + "\n"
        array = [None]*4  
        array[0] = word_type
        required_tags = ['NM', 'TRI', 'TRD']
        indices = [1, 2, 3]
    elif word_type == 'Drug':
        all_inputs += input_string + "\n"
        array = [None]*5  
        array[0] = word_type
        required_tags = ['GNM', 'TNM', 'US', 'SDE']
        indices = [1, 2, 3, 4]
    elif word_type == 'Anatomical Term':
        all_inputs += input_string + "\n"
        array = [None]*4  
        array[0] = word_type
        required_tags = ['NM', 'BP', 'UBP']
        indices = [1, 2, 3]
    elif word_type == 'None':
        array = [word_type]
        return array
    else:
        # Unknown type
        array = [word_type]
        return array

    # Extract values for the required tags
    for tag, index in zip(required_tags, indices):
        pattern = patterns.get(tag)
        match = re.search(pattern, input_string)
        if match:
            value = match.group(1)
        else:
            value = None
        array[index] = value

    return array
