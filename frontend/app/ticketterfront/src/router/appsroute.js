import Home from '@/apps/Home/Home'
import Signin from '@/apps/Signin/Signin'

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
  }
]