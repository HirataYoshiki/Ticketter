<template>
  <b-form>
    <b-form-group v-for="content in contents" :key="content.subject" :label="content.subject">
      <b-carousel controls indicators :interval="4000">
        <b-carousel-slide v-for="item in content.items" :key="item.title">
          <template #img>
            <Content :title="item.title" :img="item.src" :text="item.text"/>
          </template>
        </b-carousel-slide>
      </b-carousel>
    </b-form-group>
  </b-form>
</template>
<script>
import Content from './components/FordevContent.vue'
export default {
  name: 'fordeveloppers',
  components: { Content },
  data () {
    return {
      contents: [
        {
          subject: 'アプリの説明' ,
          items: [
            {
              title: '証明書を発行、譲渡するためのバックエンドサービス',
              text: '複数のアカウントに紐づいた個人・団体が特定の個人・団体に対して文書を与えることができます。',
              src: require('@/assets/fordevs/1.png')
            },
            {
              title: '証明書の制限',
              text: '証明書は1アカウントにつき原則3種類までしか作成できません。',
              src: require('@/assets/fordevs/2.png')
            },
            {
              title: '証明書発行数の制限',
              text: '各証明書は1つにつき最大100枚まで発行できます。発行枚数が少ないほど市場への流通が少なくなり相対的に価値が上昇します。',
              src: require('@/assets/fordevs/3.png')
            }
          ]
        },
        {
          subject: '開発者の方へのお願い',
          items: [
            {
              title: 'View層の作成',
              text: 'このWebアプリを御覧の方はすでにお気づきだと思われますが、当開発者はUX/UIのセンスがありません。このアプリのコンセプトに賛同いただける方はぜひ\
              当アプリケーションのUI/UXを作ってみませんか？',
              src: require('@/assets/fordevs/4.png')
            },
            {
              title: 'RESTAPIの利用',
              text: '当アプリケーションはデータのCRUDにRESTAPIを使用しています。ご利用をご検討いただける方は開発者にご連絡ください。チケットのCRUDに関するRESTAPIを公開いたします。',
              src: require('@/assets/fordevs/5.png')
            },
            {
              title: '開発者様のメリット',
              text: '開発者様のアプリケーション内で発生する広告収入等は開発者様に管理いただき、当アプリケーション利用代金などとして金銭を請求しません。ただし、チケット数及びチケット発行枚数に影響を与える変更の一切については禁止とさせていただきます。',
              src: require('@/assets/fordevs/6.png')
            }
          ]
        },
        {
          subject: '利用者層の想定',
          items: [
            {
              title: '①ライト層',
              text: '娯楽目的のユーザー層。証明書のやりとり、保有を主とする若年層。',
              src: require('@/assets/fordevs/7.png')
            },
            {
              title: '②ミドル層',
              text: '他のコミュニティーにて知名度のある個人。当アプリケーションを個人株のような形で利用する。証明書の販売を主とする。',
              src: require('@/assets/fordevs/8.png')
            },
            {
              title: '③法人',
              text: '資格や在籍証明として利用する。',
              src: require('@/assets/fordevs/9.png')
            }
          ]
        }
      ]
    }
  }
}
</script>