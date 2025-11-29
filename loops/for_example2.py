
chaine = "a digital system is a something that represents information by using digits. Each digit represents a small amount of information because each digit comes from a small set of choices. A digit can be decimal (one of the ten choices from 0 through 9), as in the display of a digital clock. A digit can be binary (either 0 or 1). A binary digit is called a bit. Digital computers and digital communication like the internet usually use binary. The meaning of each bit depends on the place where it is used. For example, a bit can represent 'Yes' or 'No', or it can represent 'True' or 'False'. A large amount of information, like a picture, can be represented by using a list of many bits."

n_count = 0
m_count = 0

for caractere in chaine:
    print(caractere)
    if caractere == "n":
        n_count+=1
    elif caractere == "m":
        m_count+=1 # m_count = m_count + 1

print("Count n = ", n_count)
print("Count m = ", m_count)
