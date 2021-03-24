<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ActorSystem extends Model
{
    /**
     * @description EventType
     *
     * @var string
     */
    public $eventType;
    protected $_name = [
        'eventType' => 'event_type',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->eventType) {
            $res['event_type'] = $this->eventType;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ActorSystem
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['event_type'])) {
            $model->eventType = $map['event_type'];
        }

        return $model;
    }
}
