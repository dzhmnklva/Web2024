// company.model.ts

export interface Company {
    id: number;
    name: string;
    description: string;
    city: string;
    address: string;
  }
  
  // vacancy.model.ts
  
  export interface Vacancy {
    id: number;
    name: string;
    description: string;
    salary: number;
    company: Company;
  }
  