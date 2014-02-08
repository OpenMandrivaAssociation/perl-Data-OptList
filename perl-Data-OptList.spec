%define upstream_name    Data-OptList
%define upstream_version 0.107

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Parse and validate simple name/value option pairs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl-devel

BuildArch:	noarch

%description 
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Data
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.107.0-3mdv2012.0
+ Revision: 765146
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.107.0-2
+ Revision: 763660
- rebuilt for perl-5.14.x

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.107.0-1
+ Revision: 672611
- update to new version 0.107

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.106.0-2
+ Revision: 667081
- mass rebuild

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.106.0-1mdv2011.0
+ Revision: 506236
- update to 0.106

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.105.0-1mdv2010.1
+ Revision: 491627
- update to 0.105

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.104-2mdv2010.0
+ Revision: 440544
- rebuild

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.104-1mdv2009.1
+ Revision: 330405
- update to new version 0.104

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.103-3mdv2009.0
+ Revision: 256473
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.103-1mdv2008.1
+ Revision: 106565
- update to new version 0.103
- update to new version 0.103

* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.102-1mdv2008.0
+ Revision: 74593
- import perl-Data-OptList


* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.102-1mdv2008.0
- first mdv release
