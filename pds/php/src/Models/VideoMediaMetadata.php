<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoMediaMetadata extends Model
{
    /**
     * @description Duration
     *
     * @example "10.111"
     *
     * @var string
     */
    public $duration;
    protected $_name = [
        'duration' => 'duration',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoMediaMetadata
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['duration'])) {
            $model->duration = $map['duration'];
        }

        return $model;
    }
}
