import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TriagemComponent } from './components/triagem/triagem.component';
import { SintomasComponent } from './components/sintomas/sintomas.component';


const routes: Routes = [
  {
    path: '',
    component: TriagemComponent
  },{
    path: ':idDiagnostico/sintomas',
    component: SintomasComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TriagemRoutingModule { }
