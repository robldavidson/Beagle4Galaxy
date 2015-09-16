import os
import optparse
import tempfile
import shutil
from subprocess import call
import gzip 

def main():
  
    parser = optparse.OptionParser()
    parser.add_option('--jar', dest='jarfile', default=None)
    parser.add_option('--gtgl',dest='gtgl',default='gt')
    parser.add_option('--gfile',dest='gfile',default=None)
    parser.add_option('--ref', dest='ref',default=None )
    parser.add_option('--impute-its',dest='impits', default="5")
    parser.add_option('--phase-its',dest='phits',default="5")
    parser.add_option('--out', dest='outfile', default='out.beagle4')
	
    (options, args) = parser.parse_args()

    if not options.jarfile:
    	parser.error('Jar option is not optional. Please provide full path to beagle4 jar file')

    if not options.gfile:
        parser.error('Genotype file not optional. Can be genotype or genotype likelihood. Please provide --gfile argument.')

    print options.jarfile
    cwd = os.getcwd()
    outdir = tempfile.mkdtemp(dir=cwd)
    outprefix = 'bglout'
    
    if options.ref:
        call(['java', '-Xmx2g', '-jar', options.jarfile, 'ref='+options.ref, options.gtgl+'='+options.gfile, 'phase-its='+options.phits,'impute-its='+options.impits , 'out='+outdir+'/'+outprefix ])
    else:
    	call(['java', '-Xmx2g', '-jar', options.jarfile, options.gtgl+'='+options.gfile,'phase-its='+options.phits, 'impute-its='+options.impits , 'out='+outdir+'/'+outprefix ])
   

    #shutil.move(outdir+'/'+outprefix+'.vcf.gz',options.outfile)
    #shutil.rmtree(outdir)
    with gzip.open(outdir+os.sep+outprefix+'.vcf.gz','rb') as gzinfile:
        with open(options.outfile,'w') as vcfoutfile:
            for line in gzinfile:
                vcfoutfile.write(line)
    
    
    shutil.rmtree(outdir)



if __name__=='__main__':
    main()

