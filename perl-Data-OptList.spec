%define module  Data-OptList
%define	name	perl-%{module}
%define version 0.104
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Parse and validate simple name/value option pairs
License: 	GPL or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Params::Util)
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description 
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{__make} test

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Data
%{_mandir}/*/*

