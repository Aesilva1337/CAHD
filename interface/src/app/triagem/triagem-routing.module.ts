import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TriagemComponent } from './components/triagem/triagem.component';


const routes: Routes = [
  {
    path: '',
    component: TriagemComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TriagemRoutingModule { }
