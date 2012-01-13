#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	List
%define		pnam	UtilsBy
%include	/usr/lib/rpm/macros.perl
Summary:	List::UtilsBy - higher-order list utility functions
#Summary(pl.UTF-8):	
Name:		perl-List-UtilsBy
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df0226ccd6f8ebf8b5965e408dca8662
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/List-UtilsBy/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a number of list utility functions, all of which
take an initial code block to control their behaviour. They are
variations on similar core perl or List::Util functions of similar
names, but which use the block to control their behaviour. For
example, the core Perl function sort takes a list of values and
returns them, sorted into order by their string value. The sort_by
function sorts them according to the string value returned by the
extra function, when given each value.

 my @names_sorted = sort @names;

 my @people_sorted = sort_by { $_->name } @people;

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/List/*.pm
%{_mandir}/man3/*
