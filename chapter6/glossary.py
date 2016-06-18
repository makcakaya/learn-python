terms = {
    'list': 'A data structure containing a collection of objects.',
    'boolean': 'A data type that can have either True or False value.',
    'dictionary': 'A data structure that can hold many key-value pairs.',
    'for loop': 'A programming mechanism to iterate through elements' 
        + ' of a container.',
    'python': 'A general use scripting language that is cross platform.',
    'computer': 'A device that can evaluate logical operations',
    'server': 'A central and powerful computer that serves other computers',
    'client': 'A computer that connects to server and make requests',
    'java': 'A well-established general purpose programming language',
    'c#': 'A modern version of Java programming language, invented by Microsoft'
}

for word, meaning in terms.items():
    print(word.title() + ": " + meaning + "\n");