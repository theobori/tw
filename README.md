# 🥐 tw

A CLI to deploy server and play Teeworlds throught Docker.

## 📖 How to build and run ?

1. Install the dependencies 
   - `python` >= **3.11**
   - `docker`*

2. Install the CLI
```bash
sudo make install
```
3. Run `tw -h`

## 📜 usage example

```bash
tw server -l
tw server -k vanilla --build
tw server -k vanilla --run
tw server -k vanilla --run -p 8303 -c $PWD/autoexec.cfg

tw client --run teeworlds
```

## ℹ️ Note

This CLI assumes that youre using X with an UNIX system based.

## ✍️ TODO

| Feature | State |
:--- | :---: |
Fix package relative imports | ✅
Server custom config file | ✅
Build and install `tw` as a CLI command | ✅
Add a CLI arg to list the available keys | ✅
Mount volume client side for user dir | ✅
Forward UDP instead of TCP | ✅

<!-- ## 📜 Usage example -->

