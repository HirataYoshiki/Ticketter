import Home from '@/apps/Home/Home'
import Create from '@/apps/Create/Create'
import Profile from '@/apps/Profile/Profile'
import Interactions from '@/apps/Interactions/Interactions'
import RequestForm from '@/apps/RequestForm/RequestForm'

export const AppsRoutes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/create',
    name: 'Create',
    component: Create
  },
  {
    path: '/profile/:uid',
    name: 'profile',
    component: Profile,
    props: true
  },
  {
    path: '/interactions',
    name: 'interactions',
    component: Interactions,
    props: true
  },
  {
    path: '/form',
    name: 'requestform',
    component: RequestForm
  }
]