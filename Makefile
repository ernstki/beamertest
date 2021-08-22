BASE = slides
SOURCES = $(BASE).md defaults.yml Makefile

pdf: $(BASE).pdf

tex: $(BASE).tex

$(BASE).tex $(BASE).pdf: $(SOURCES)
	pandoc -s -i -t beamer -d defaults.yml $(BASE).md -o $@

#-V aspectratio=169            - put in defaults.yml instead
#-V theme=Copenhagen           - put in defaults.yml instead
#--slide-level 4               - create subsections; see defaults.yml
#-V navigation:frame           - add navigation controls; see defaults.yml
#--metadata-file metadata.yml  - use YAML header instead
#-V institute="Weirauch Lab"   - use YAML header instead

clean:
	# clean up TeXShop temp files
	-rm $(BASE).{aux,log,nav,out,snm,synctex.gz,toc}

reallyclean: clean
	-rm $(BASE).{tex,pdf}
