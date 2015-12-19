#!/usr/bin/perl

print "Starting.\n";
open (IN, "xscreensaver-command -watch 2<&1 |");
while (<IN>) {
    print $_;
    if (m/^(BLANK|LOCK)/) {
	print "Blanking display.\n";
        system "./blank_display.sh";    
    } elsif (m/^UNBLANK/) {
	print "Unblanking display.\n";
	system "./unblank_display.sh";
    }
}
