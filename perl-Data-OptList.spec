%define modname	Data-OptList
%define modver 0.112

Summary:	Parse and validate simple name/value option pairs
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Data::OptList
Source0:	http://www.cpan.org/modules/by-module/Data/Data-OptList-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Params::Util)

%description 
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*


