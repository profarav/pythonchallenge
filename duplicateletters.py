def no_duplicate_letters(phrase):
	return all(len(set(i)) == len(i) for i in phrase.split())
    
phrase = "happy plus"
