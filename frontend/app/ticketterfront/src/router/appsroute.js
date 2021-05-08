import Home from '@/apps/Home/Home'
import Signin from '@/apps/Signin/Signin'
import Create from '@/apps/Create/Create'

export const AppsRoutes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/create',
    name: 'Create',
    component: Create
  }
]