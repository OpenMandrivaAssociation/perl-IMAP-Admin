%define upstream_name    IMAP-Admin

Name:		perl-%{upstream_name}
Version:	1.6.8
Release:	1

Summary:	IMAP-Admin Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/IMAP/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
A perl module to manage IMAP servers.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%files
%doc Changes examples
%defattr(-, root, root)
%{perl_vendorlib}/IMAP/*
%{_mandir}/*/*
