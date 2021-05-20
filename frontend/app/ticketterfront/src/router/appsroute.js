import Create from '@/apps/Create/Create'
import Profile from '@/apps/Profile/Profile'
import Users from '@/apps/Users/Users'
import Interactions from '@/apps/Interactions/Interactions'
import RequestForm from '@/apps/RequestForm/RequestForm'
import ForDeveloppers from '@/apps/ForDeveloppers/ForDeveloppers'

export const AppsRoutes = [
  {
    path: '/',
    name: 'Home',
    component: Profile,
    props: {
      me: true
    }
  },
  {
    path: '/create',
    name: 'Create',
    component: Create
  },
  {
    path: '/users',
    name: 'users',
    component: Users
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
  },
  {
    path: '/fordevs',
    name: 'fordevs',
    component: ForDeveloppers
  }
]