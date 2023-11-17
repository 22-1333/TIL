import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import InterestView from '@/views/InterestView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import BankView from '@/views/BankView.vue'
import DepositListView from '@/views/DepositListView.vue'
import InstallmentSavingListView from '@/views/InstallmentSavingListView.vue'
import InterestDetailView from '@/views/InterestDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/interest',
      name: 'interest',
      component: InterestView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/bank',
      name: 'bank',
      component: BankView
    },
    {
      path: '/interest/deposit_list',
      name: 'depositList',
      component: DepositListView
    },
    {
      path: '/interest/installment_saving_list',
      name: 'installmentSavingList',
      component: InstallmentSavingListView
    },
    {
      path: '/interest/:fin_prdt_cd',
      name: 'interestDetail',
      component: InterestDetailView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView
    }
  ]
})

export default router
