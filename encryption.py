Codons = {
	"A" : "GCT", "S" : "GTT",
	"B" : "TGT", "T" : "TGG",
	"C" : "GAT", "U" : "TAT",
	"D" : "GAA", "V" : "GCC",
	"E" : "TTT", "W" : "TGC",
	"F" : "GGT", "X" : "GAC",
	"G" : "GCA", "Y" : "GAG", 
	"H" : "CAT", "Z" : "ATT",
	"I" : "ATA",
	"J" : "TTT",
	"K" : "TTA",
	"L" : "ATG",
	"M" : "AAU",
	"N" : "CCT",
	"O" : "CAA",
	"P" : "CGT",
	"Q" : "TCT",
	"R" : "ACT",
	"1" : "AAG", "2" : "TTG", "3" : "CTT",
	"4" : "CTC", "5" : "CTA", "6" : "CTG",
	"7" : "AAC", "8" : "CCC", "9" : "CCA",
	"." : "CGC", "," : "CGA",
	"?" : "ACA", "!" : "GTG",
	" " : "GTA", "@" : "TAC"
}


def encryption(msg,index=0):
	res = ''.join(Codons[msg[i]] for i in range(index,len(msg)))
	return res 

def mainFunc():
	secret = input("Enter your secret message: \n")
	encr = encryption(secret.upper())
	print("Your Stego DNA sequence is: \n")
	print(encr)

if  __name__  == "__main__":
	mainFunc() 


#Reference Google Scholar: DNA Based Steganography