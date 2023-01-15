%define modname	Data-OptList

Summary:	Parse and validate simple name/value option pairs
Name:		perl-%{modname}
Version:	0.113
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Data::OptList
Source0:	http://www.cpan.org/modules/by-module/Data/Data-OptList-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Params::Util)

%description 
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Data
%{_mandir}/man3/*
