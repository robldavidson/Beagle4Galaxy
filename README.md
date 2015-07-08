# Beagle4Galaxy
A simple Galaxy wrapped implementation of Beagle4.0 

Installation
============

This tool is available from the Main Galaxy Toolshed. Please search for 'beagle4' at the ToolShed or visit the link: https://toolshed.g2.bx.psu.edu/repos/bobbledavidson/beagle4_0

Alternatively, download the 3 files from this repository (beagle4.py, beagle4.xml, beagle.r1399.rar) and place them in a tool folder within your galaxy installation. Remember to tell Galaxy that the new tools have been placed there if doing this manually (add the location of the beagle4.xml file to your tool_conf.xml file)


Guide
=====

Disclaimer: I have not created or worked on the Beagle 4.0 tool itself. Simply wrapped it for Galaxy. Full credit goes to the Beagle4.0 team at http://faculty.washington.edu/browning/beagle/beagle.html

For a full guide, go to the Beagle4.0 documentation here: http://faculty.washington.edu/browning/beagle/beagle.03Mar15.pdf

This wrapper allows for the selection of either a Genotype (gt) file, a Genotype Likelihood (gl) file or a Genotype (gt) plus Reference file as per the example usage here: http://faculty.washington.edu/browning/beagle/run.beagle.r1399.example

The only parameters currently exposed by this wrapper are impute-its and phase-its which both have default of 5. Please feel free to request more parameters to be made available by contacting bobbledavidson @ github. 

Test-Data
=========
The test-data folder contains 3 vcf.gz files for testing the tool. These are again copied from the Beagle4.0 example page (see above). 
test.r1399.vcf.gz should be used either as either gt or gl file in the non-reference use case
ref.r1399.vcf.gz and target.r1399.vcf.gz should be used as the gt and reference files in the +reference use case


