#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	List
%define		pnam	UtilsBy
Summary:	List::UtilsBy - higher-order list utility functions
Summary(pl.UTF-8):	List::UtilsBy - funkcje narzędziowe do list wyższego poziomu
Name:		perl-List-UtilsBy
Version:	0.12
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	54a8c7092bc02f29ea6c5ae215eea385
URL:		https://search.cpan.org/dist/List-UtilsBy/
BuildRequires:	perl-Module-Build >= 0.4004
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a number of list utility functions, all of which
take an initial code block to control their behaviour. They are
variations on similar core Perl or List::Util functions of similar
names, but which use the block to control their behaviour. For
example, the core Perl function sort takes a list of values and
returns them, sorted into order by their string value. The sort_by
function sorts them according to the string value returned by the
extra function, when given each value.

%description -l pl.UTF-8
Ten moduł udostępnia sporo funkcji narzędziowych do list,
przyjmujących początkowy blok kodu sterujący ich zachowaniem. Są to
warianty podobnych funkcji podstawowych Perla lub List::Util o
podobnych nazwach, ale wykorzystujące blok do sterowania zachowaniem.
Na przykład, funkcja podstawowa Perla sort przyjmuje listę wartości i
je zwraca w kolejności posortowanej według wartości jako łańcuchów.
Funkcja sort_by sortuje wartości według wartości łańcucha zwracanej
przez dodatkową funkcję, której przekazywana jest każda wartość.

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
%{perl_vendorlib}/List/UtilsBy.pm
%{_mandir}/man3/List::UtilsBy.3pm*
