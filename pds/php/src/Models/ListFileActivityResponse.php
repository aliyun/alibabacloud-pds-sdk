<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list file activity response.
 */
class ListFileActivityResponse extends Model
{
    /**
     * @description Activities
     *
     * @var FileActivity[]
     */
    public $activities;

    /**
     * @description NextMarker
     *
     * @var string
     */
    public $nextMarker;
    protected $_name = [
        'activities' => 'activities',
        'nextMarker' => 'next_marker',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->activities) {
            $res['activities'] = [];
            if (null !== $this->activities && \is_array($this->activities)) {
                $n = 0;
                foreach ($this->activities as $item) {
                    $res['activities'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->nextMarker) {
            $res['next_marker'] = $this->nextMarker;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListFileActivityResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['activities'])) {
            if (!empty($map['activities'])) {
                $model->activities = [];
                $n                 = 0;
                foreach ($map['activities'] as $item) {
                    $model->activities[$n++] = null !== $item ? FileActivity::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['next_marker'])) {
            $model->nextMarker = $map['next_marker'];
        }

        return $model;
    }
}
