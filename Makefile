PREFIX_DIR = /usr/local
PREFIX_BIN = $(PREFIX_DIR)/bin

# Symlink destination
LINK = $(PREFIX_BIN)/tw

# Main script
MAIN = tw/__main__.py

# Scripts path
OPT_DIR = $(PREFIX_DIR)/opt/tw_cli

init:
	test -d $(PREFIX_BIN) || mkdir -p $(PREFIX_BIN)
	test -d $(OPT_DIR) || mkdir -p $(OPT_DIR)

	chmod +x $(MAIN)

####################
# Install scripts
####################

install: init
	cp -r tw/ images/ $(OPT_DIR)
	ln -s $(OPT_DIR)/$(MAIN) $(LINK)

####################
# Uninstall scripts
####################

clean:
	$(RM) $(LINK)

uninstall: clean
	$(RM) -r $(OPT_DIR)

re: uninstall install

.PHONY: init clean install uninstall re help
