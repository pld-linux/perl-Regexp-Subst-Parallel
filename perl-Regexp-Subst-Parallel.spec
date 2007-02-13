#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Subst-Parallel
Summary:	Regexp::Subst::Parallel - multiple substitutions on a string in parallel
Summary(pl.UTF-8):	Regexp::Subst::Parallel - jednoczesne wykonywanie wielu podstawień w łańcuchu
Name:		perl-Regexp-Subst-Parallel
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ebebdad0aea5835daeb8e3cb7add383e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Subst::Parallel is a module that allows you to make multiple
simultaneous substitutions safely. Using the sole exported subst
function has a rather different effect from doing each substitution
sequentially.

%description -l pl.UTF-8
Regexp::Subst::Parallel to moduł pozwalający na bezpieczne wykonywanie
wielu podstawień jednocześnie. Użycie zwykłej funkcji subst daje
raczej inny efekt niż wykonywanie podstawień sekwencyjnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/%{pdir}/Subst
%{perl_vendorlib}/%{pdir}/Subst/Parallel.pm
%{_mandir}/man3/*
