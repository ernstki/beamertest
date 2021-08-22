BASE = slides
SOURCES = $(BASE).md defaults.yml Makefile

all: pdf tex readme

pdf: $(BASE).pdf

tex: $(BASE).tex

readme: README.md

README.md: $(SOURCES)
	pandoc -t gfm -F mermaid-filter $(BASE).md > $@

$(BASE).tex $(BASE).pdf: $(SOURCES)
	pandoc -s -i -F mermaid-filter -t beamer -d defaults.yml $(BASE).md -o $@
	
	# now make the PDF version of the mermaid diagram(s) for Beamer slides
	for svg in img/*.svg; do svg2pdf "$${svg%.svg}."{svg,pdf}; done

#-V aspectratio=169            - put in defaults.yml instead
#-V theme=Copenhagen           - put in defaults.yml instead
#--slide-level 4               - create subsections; see defaults.yml
#-V navigation:frame           - add navigation controls; see defaults.yml
#--metadata-file metadata.yml  - use YAML header instead
#-V institute="Weirauch Lab"   - use YAML header instead

clean:
	# clean up TeXShop temp files
	-rm $(BASE).{aux,log,nav,out,snm,synctex.gz,toc}
	-rm mermaid-filter.err

reallyclean: clean
	-rm $(BASE).{tex,pdf}
