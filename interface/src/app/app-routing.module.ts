import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TriagemComponent } from './triagem/components/triagem/triagem.component';
import { HomeComponent } from './home/home.component';
import { TemplateComponent } from './template/template.component';


const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent,
    children: [
      {
        path: 'triagem',
        loadChildren: './triagem/triagem.module#TriagemModule'
      }
    ]
  },{
    path: '',
    redirectTo: '/home/triagem',
    pathMatch: 'full'
  },
  {
    path: 'template',
    component: TemplateComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
