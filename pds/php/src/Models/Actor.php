<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class Actor extends Model
{
    /**
     * @var ActorAliUser
     */
    public $aliUser;

    /**
     * @var ActorAnonymousUser
     */
    public $anonymousUser;

    /**
     * @var ActorSystem
     */
    public $system;

    /**
     * @var ActorUser
     */
    public $user;
    protected $_name = [
        'aliUser'       => 'ali_user',
        'anonymousUser' => 'anonymous_user',
        'system'        => 'system',
        'user'          => 'user',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->aliUser) {
            $res['ali_user'] = null !== $this->aliUser ? $this->aliUser->toMap() : null;
        }
        if (null !== $this->anonymousUser) {
            $res['anonymous_user'] = null !== $this->anonymousUser ? $this->anonymousUser->toMap() : null;
        }
        if (null !== $this->system) {
            $res['system'] = null !== $this->system ? $this->system->toMap() : null;
        }
        if (null !== $this->user) {
            $res['user'] = null !== $this->user ? $this->user->toMap() : null;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return Actor
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['ali_user'])) {
            $model->aliUser = ActorAliUser::fromMap($map['ali_user']);
        }
        if (isset($map['anonymous_user'])) {
            $model->anonymousUser = ActorAnonymousUser::fromMap($map['anonymous_user']);
        }
        if (isset($map['system'])) {
            $model->system = ActorSystem::fromMap($map['system']);
        }
        if (isset($map['user'])) {
            $model->user = ActorUser::fromMap($map['user']);
        }

        return $model;
    }
}
