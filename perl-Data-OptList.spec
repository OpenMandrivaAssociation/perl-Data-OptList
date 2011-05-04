%define upstream_name    Data-OptList
%define upstream_version 0.106

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	Parse and validate simple name/value option pairs
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Params::Util)

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description 
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Data
%{_mandir}/*/*
