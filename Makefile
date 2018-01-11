#MAKEFILE OF CRYPTO-FETCHER

#DEFINIZIONE DEL COMPILATORE
CXX	= g++
#OPZIONI DEL COMPILATORE
CFLAGS = -pipe -std=c++14 -O2 -lcurl
#IDENTIFICA TUTTI I FILE DA CUI IL PROGRAMMA DIPENDE
OBJECTS = main.o

#ISTRUZIONI PER L'ESEGUIBILE
all: $(OBJECTS)
	 @echo -e "\033[1;34m"COSTRUZIONE DELL"'" ESEGUIBILE IN CORSO..." \033[0m"
	 $(CXX) $(CFLAGS) $(OBJECTS) -o crypto-fecther
	 @echo -e "\033[1;34m"ESEGUIBILE COSTRUITO" \033[0m"
	 $(MAKE) clean
	 @echo -e "\033[1;34m"COMPILAZIONE TERMINATA" \033[0m"


#ISTRUZIONI PER COMPILARE LE VARIE CLASSI
%.o: %.cpp
	 $(CXX) $(CFLAGS) -c $^ -o $@
	 
#ISTRUZIONI PER ELIMINARE I FILE *.o
clean: 
	 @echo -e "\033[1;34m"RIMOZIONE DEI BINARI IN CORSO..." \033[0m"
	 $(RM) $(OBJECTS)
	 @echo -e "\033[1;34m"RIMOZIONE TERMINATA" \033[0m"