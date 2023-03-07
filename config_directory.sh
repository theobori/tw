#!/usr/bin/env bash

# Source: DDNET release
function config_directory() {
	local dirpath

	case "$(uname -s)" in
		CYGWIN*|MINGW*|MSYS*)
			if [ -d "$APPDATA/DDNet/" ]; then
				dirpath="$APPDATA/DDNet/"
			else
				dirpath="$APPDATA/Teeworlds/"
			fi;;
		
		Darwin*)
			if [ -d "$HOME/Library/Application Support/DDNet/" ]; then
				dirpath="$HOME/Library/Application Support/DDNet/"
			else
				dirpath="$HOME/Library/Application Support/Teeworlds/"
			fi;;
		
		*)
			DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
			if [ -d "$DATA_HOME/ddnet/" ]; then
				dirpath="$DATA_HOME/ddnet/"
			else
				dirpath="$HOME/.teeworlds/"
			fi;;
	esac

	printf "$dirpath"
}
