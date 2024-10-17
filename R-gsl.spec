%global packname gsl
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 1.9_9
Release: 1
Summary: Wrapper for the Gnu Scientific Library
Group: Sciences/Mathematics
License: GPLv2+
URL: https://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_1.9-9.tar.gz
Requires: R-core 
BuildRequires: R-devel texlive-collection-latex 
%ifarch i586
Requires: libgsl0 >= 1.12
BuildRequires: libgsl0 >= 1.12 libgsl-devel
%endif
%ifarch x86_64
Requires: lib64gsl0 >= 1.12
BuildRequires: lib64gsl0 >= 1.12 lib64gsl-devel
%endif

%description
An R wrapper for the special functions and quasi random
number generators of the Gnu Scientific Library
(http://www.gnu.org/software/gsl/). See gsl-package.Rd for
details of overall package organization, and Misc.Rd for some
functions that are widely used in the package, and some tips on installation.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
